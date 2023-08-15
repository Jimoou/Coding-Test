class Solution {
    public static int[] solution(String[] park, String[] routes) {
        int x = 0;
        int y = 0;

        for (int i = 0; i < park.length; i++) {
            if (park[i].indexOf('S') != -1) {
                x = i;
                y = park[i].indexOf('S');
                break;
            }
        }

        for (String route : routes) {
            String[] command = route.split(" ");
            char dir = command[0].charAt(0);
            int dist = Integer.parseInt(command[1]);

            switch (dir) {
                case 'N':
                    if (isMovableNorth(park, x, y, dist)) {
                        x -= dist;
                    }
                    break;
                case 'S':
                    if (isMovableSouth(park, x, y, dist)) {
                        x += dist;
                    }
                    break;
                case 'W':
                    if (isMovableWest(park, x, y, dist)) {
                        y -= dist;
                    }
                    break;
                case 'E':
                    if (isMovableEast(park, x, y, dist)) {
                        y += dist;
                    }
                    break;
            }
        }

        return new int[]{x, y};
    }
    // 이동 가능한지 검사하는 메소드
    private static boolean isMovableNorth(String[] park, int x, int y, int dist) {
        for (int i = 1; i <= dist; i++) {
            if (x - i < 0 || park[x - i].charAt(y) == 'X') {
                return false;
            }
        }
        return true;
    }

    private static boolean isMovableSouth(String[] park, int x, int y, int dist) {
        for (int i = 1; i <= dist; i++) {
            if (x + i >= park.length || park[x + i].charAt(y) == 'X') {
                return false;
            }
        }
        return true;
    }

    private static boolean isMovableWest(String[] park, int x, int y, int dist) {
        for (int i = 1; i <= dist; i++) {
            if (y - i < 0 || park[x].charAt(y - i) == 'X') {
                return false;
            }
        }
        return true;
    }

    private static boolean isMovableEast(String[] park, int x, int y, int dist) {
        for (int i = 1; i <= dist; i++) {
            if (y + i >= park[0].length() || park[x].charAt(y + i) == 'X') {
                return false;
            }
        }
        return true;
    }
}




