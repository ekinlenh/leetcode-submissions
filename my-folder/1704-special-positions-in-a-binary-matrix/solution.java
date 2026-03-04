class Solution {
    public int numSpecial(int[][] mat) {
        boolean[] row = new boolean[mat.length];  
        boolean[] col = new boolean[mat[0].length];

        for (int i = 0; i < row.length; i++) {
            int count = 0;
            for (int j = 0; j < col.length; j++) {
                if (mat[i][j] == 1) count++;
            }

            if (count == 1) row[i] = true;
        }

        for (int i = 0; i < col.length; i++) {
            int count = 0;
            for (int j = 0; j < row.length; j++) {
                if (mat[j][i] == 1) count++;
            }

            if (count == 1) col[i] = true;
        }

        int res = 0;
        for (int i = 0; i < row.length; i++) {
            for (int j = 0; j < col.length; j++) {
                if (mat[i][j] == 1 && row[i] && col[j]) {
                        res++;
                    }
            }
        }

        return res;
    }
}
