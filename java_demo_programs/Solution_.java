import java.util.HashMap;
import java.util.Map;

public class Solution_ {
    public static void main(String[] args) {
        String s = "abdef";
        String s1 = s.substring(1, s.length() - 1);
        // s1 = "";
        System.out.println(s1);
        // int a = 1;
        // int b = a / 0;
        int[] a = null;
        a[4] = 4;
    }

    public static void test1() {
        System.out.println("=======test1=======");
        String[] commands = {
                "PUT key1 5",
                "PUT key2 6",
                "GET key1",
                "GET key1 1",
                "GET key2 2",
                "PUT key1 7",
                "GET key1 1",
                "GET key1 2",
                "GET key1 3",
                "GET key4",
                "GET key1 4",
                "GET key2 1" };
        Service service = new Service();
        for (String cmd : commands) {
            String res = service.operate(cmd);
            System.out.println(res);
        }
    }

    public static void test2() {
        System.out.println("========test2========");
        String[] commands = {
                "PUT key1 five",
                "PUT key2 6",
                "PUT key3",
                "GET key1",
                "GET key2 five",
                "PATCH" };
        Service service = new Service();
        for (String cmd : commands) {
            String res = service.operate(cmd);
            System.out.println(res);
        }
    }
}

class Service {
    VersionedMap map;

    public Service() {
        map = new VersionedMap();
    }

    public String operate(String command) {
        String[] commands = command.split(" ");

        if (commands[0].equals("PUT") && commands.length == 3) {
            try {
                int version = Integer.parseInt(commands[2]);
                return this.put(commands[1], version);
            } catch (NumberFormatException e) {
                return "invalid argument format: " + command;
            }
        } else if (commands[0].equals("GET") && commands.length == 2) {
            return this.get(commands[1]);
        } else if (commands[0].equals("GET") && commands.length == 3) {
            try {
                int version = Integer.parseInt(commands[2]);
                return this.get(commands[1], version);
            } catch (NumberFormatException e) {
                return "invalid argument format: " + command;
            }
        } else {
            return "invalid command";
        }
    }

    public String put(String key, int value) {
        int version = map.put(key, value);
        return "PUT(#" + version + ") " + key + " = " + value;
    }

    public String get(String key) {
        Integer value = map.get(key);
        String res;
        if (value == null) {
            res = "<NULL>";
        } else {
            res = String.valueOf(value);
        }
        return "GET " + key + " = " + res;
    }

    public String get(String key, int version) {
        Integer value = map.get(key, version);
        String res;
        if (value == null) {
            res = "<NULL>";
        } else {
            res = String.valueOf(value);
        }
        return "GET " + key + "(#" + version + ") = " + res;
    }
}

class VersionedMap {
    private static int version = 1;
    private Map<String, Integer> latestMap;
    private Map<String, Integer> versionMap;

    public VersionedMap() {
        latestMap = new HashMap<>();
        versionMap = new HashMap<>();
    }

    public int put(String key, int value) {
        int currentVersion = version;
        versionMap.put(key + ":" + currentVersion, value);
        latestMap.put(key, value);
        version += 1;
        return currentVersion;
    }

    public Integer get(String key, int version) {
        if (!latestMap.containsKey(key)) {
            return null;
        }

        int currentVersion = version;
        String combinedKey = key + ":" + currentVersion;

        while (!versionMap.containsKey(combinedKey) && currentVersion != 0) {
            currentVersion -= 1;
            combinedKey = key + ":" + currentVersion;
        }
        return versionMap.get(combinedKey);
    }

    public Integer get(String key) {
        if (latestMap.containsKey(key)) {
            return latestMap.get(key);
        }

        return null;
    }
}
