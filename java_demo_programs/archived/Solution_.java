package archived;

import java.util.LinkedList;
import java.util.Queue;

public class Solution_ {
    public static void main(String[] args) {
        // archived.Car car = new archived.Car();
        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);
        queue.add(2);
        queue.size();
        queue.isEmpty();
        System.out.println(queue.poll());
    }

}

class SportCar implements Car {
    public void printCar() {

    }
}

interface Car {
    public void printCar();
}

// class archived.Car {
// String name;

// public archived.Car(String name) {
// this.name = name;
// }

// public String toString() {
// return name;
// }
// }
// class Service {
// VersionedMap map;

// public Service() {
// map = new VersionedMap();
// }

// public String operate(String command) {
// String[] commands = command.split(" ");

// if (commands[0].equals("PUT") && commands.length == 3) {
// try {
// int version = Integer.parseInt(commands[2]);
// return this.put(commands[1], version);
// } catch (NumberFormatException e) {
// return "invalid argument format: " + command;
// }
// } else if (commands[0].equals("GET") && commands.length == 2) {
// return this.get(commands[1]);
// } else if (commands[0].equals("GET") && commands.length == 3) {
// try {
// int version = Integer.parseInt(commands[2]);
// return this.get(commands[1], version);
// } catch (NumberFormatException e) {
// return "invalid argument format: " + command;
// }
// } else {
// return "invalid command";
// }
// }

// public String put(String key, int value) {
// int version = map.put(key, value);
// return "PUT(#" + version + ") " + key + " = " + value;
// }

// public String get(String key) {
// Integer value = map.get(key);
// String res;
// if (value == null) {
// res = "<NULL>";
// } else {
// res = String.valueOf(value);
// }
// return "GET " + key + " = " + res;
// }

// public String get(String key, int version) {
// Integer value = map.get(key, version);
// String res;
// if (value == null) {
// res = "<NULL>";
// } else {
// res = String.valueOf(value);
// }
// return "GET " + key + "(#" + version + ") = " + res;
// }
// }

// class VersionedMap {
// private static int version = 1;
// private Map<String, Integer> latestMap;
// private Map<String, Integer> versionMap;

// public VersionedMap() {
// latestMap = new HashMap<>();
// versionMap = new HashMap<>();
// }

// public int put(String key, int value) {
// int currentVersion = version;
// versionMap.put(key + ":" + currentVersion, value);
// latestMap.put(key, value);
// version += 1;
// return currentVersion;
// }

// public Integer get(String key, int version) {
// if (!latestMap.containsKey(key)) {
// return null;
// }

// int currentVersion = version;
// String combinedKey = key + ":" + currentVersion;

// while (!versionMap.containsKey(combinedKey) && currentVersion != 0) {
// currentVersion -= 1;
// combinedKey = key + ":" + currentVersion;
// }
// return versionMap.get(combinedKey);
// }

// public Integer get(String key) {
// if (latestMap.containsKey(key)) {
// return latestMap.get(key);
// }

// return null;
// }
// }
