public class ComplexNumber {
    private int a;
    private int b;

    public ComplexNumber(int a, int b) {
        this.a = a;
        this.b = b;
    }

    public int getA() {
        return a;
    }

    public int getB() {
        return b;
    }

    public ComplexNumber add(ComplexNumber input) {
        return new ComplexNumber(this.a + input.getA(), this.b + input.getB());
    }

    public ComplexNumber multiply(ComplexNumber input) {
        return new ComplexNumber(a * input.getA() - b * input.getB(), a * input.getB() + b * input.getA());
    }

}

public CoionCollectionTools(String country, int rows, int columns) {
    coinBox = new Coin[rows][columns];
    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < columns; col++) {
            coinBox[row][col] = new Coin(country, 0, 0);
        }
    }
}

    public Coin[][] fillCoinBox(ArrayList<Coin> myCoins) {
        for (int i = 0; i < myCoins.size(); i++) {
            int row = i % coinBox.length;
            int column = i / coinBox.length;
            coinBox[row][column] = myCoins.get(i);
        }
    }

public ArrayList<Coin> fillCoinTypeList() {
    ArrayList<Coin> result = new ArrayList<>();

    for (int i = 0; i < coinBox.length; i++) {
        for (int j = 0; j < coinBox[i].length; j++) {
            for (int type = 1; type <= 6; type++) {
                if (coinBox[i][j].getCoinType() == type) {
                    result.add(coinBox[i][j]);
                }
            }
        }
    }
    
    return result;
}
