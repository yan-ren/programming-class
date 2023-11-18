public class Day {    
    int day;

    public void setDay(String day) {
        if (day.equals("Monday")) {
            this.day = 0;
        }
    }

    private String getDayFromNumber(int number) {
        if (number == 0) {
            return "Monday";
        }else if (number == 1) {
            return "Tuesday";
        }
    }

    public String getDay() {
        return getDayFromNumber(day);
    }

    public String getNextDay() {
        return getDayFromNumber((day + 1) % 7);
    }

    public String getPreviousDay() {
        return getDayFromNumber(((day - 1) + 7) % 7);
    }

    public String addDays(int days) {
        return getDayFromNumber((day + days) % 7);
    }
}
