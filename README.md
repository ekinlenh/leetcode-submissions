# LeetCode Sync

GitHub Action for automatically syncing LeetCode submissions to a GitHub repository.

## Features

- Syncs accepted solutions from LeetCode to the default branch of the GitHub repo
- Only syncs solutions that have not been synced before
- Uploads the latest accepted solution for a single problem if there are multiple submissions per day

## How to use

1. Login to LeetCode and obtain the `csrftoken` and `LEETCODE_SESSION` cookie values.

   - After logging in, right-click on the page and press `Inspect`.
   - Refresh the page.
   - Look for a network request to https://leetcode.com.
   - Look under `Request Headers` for the `cookie:` attribute to find the values.

2. Create a new GitHub repository to host the LeetCode submissions.

   - It can be either private or public.

3. Add the values from step 1 as [GitHub secrets](https://docs.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets#creating-encrypted-secrets-for-a-repository),
   e.g. `LEETCODE_CSRF_TOKEN` and `LEETCODE_SESSION`.

4. Go to REPO > settings > actions and in Workflow Permissions section give actions Read and Write permissions.

5. Add a workflow file with this action under the `.github/workflows` directory, e.g. `sync_leetcode.yml`.

   Example workflow file:

   ```yaml
   name: Sync Leetcode

   on:
     workflow_dispatch:
     schedule:
       - cron: "0 8 * * 6"

   jobs:
     build:
       runs-on: ubuntu-latest

       steps:
         - name: Sync
           uses: joshcai/leetcode-sync@v1.7
           with:
             github-token: ${{ github.token }}
             leetcode-csrf-token: ${{ secrets.LEETCODE_CSRF_TOKEN }}
             leetcode-session: ${{ secrets.LEETCODE_SESSION }}
             destination-folder: my-folder
             verbose: true
             commit-header: "[LeetCode Sync]"
   ```

6. After you've submitted a LeetCode solution, run the workflow by going to the `Actions` tab, clicking the action name, e.g. `Sync Leetcode`, and then clicking `Run workflow`. The workflow will also automatically run once a week by default (can be configured via the `cron` parameter).

## Inputs

- `github-token` _(required)_: The GitHub access token for pushing solutions to the repository
- `leetcode-csrf-token` _(required)_: The LeetCode CSRF token for retrieving submissions from LeetCode
- `leetcode-session` _(required)_: The LeetCode session value for retrieving submissions from LeetCode
- `filter-duplicate-secs`: Number of seconds after an accepted solution to ignore other accepted solutions for the same problem, default: 86400 (1 day)
- `destination-folder` _(optional)_: The folder in your repo to save the submissions to (necessary for shared repos), default: _none_
- `verbose` _(optional)_: Adds submission percentiles and question numbers to the repo (requires an additional API call), default: true
- `commit-header` _(optional)_: How the automated commits should be prefixed, default: 'Sync LeetCode submission'
