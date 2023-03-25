public class Outfit extends ClothingItem {
	Shoes shoes;
	Pants pants;
	Top top;

	public Outfit (Shoes shoes, Pants pants, Top top) {
		this.shoes = shoes;
		this.pants = pants;
		this.top = top;
	}

	public String getDescription() {
		return shoes.getDescription() + "/" + pants.getDescription() +
		"/" + top.getDescription() + " outfit";
	}

	public double getPrice() {
		if (shoes.getPrice() + pants.getPrice() >= 100 || ...) {
			return 0.75*(shoes.getPrice() + pants.getPrice() + top.getPrice());
		}

		return 0.9*(shoes.getPrice() + pants.getPrice() + top.getPrice());
	}
}

public void removeNotes() {
	int i = 0;
	while (i < noteList.size()) {
		if (...) {
			noteList.remove(i);
		}else {
			i++;
		}
	}
}

public boolean twoTogether() {
	for (int row = 0; row < NUM_ROWS; row++) {
		for (int col = 0; col < SEATS_PER_ROW - 1; col++) {
			if(seats[row][col] == 0 && seats[row][col+1] == 0) {
				seats[row][col] = 1
				seats[row][col + 1] = 1
				return True;
			}
		}
	}

	return False;
}

public int findAdjacent(int row, int seatsNeeded) {
	int col = 0;
	int min = col;
	int count = 0;

	while (col < SEATS_PER_ROW) {
		int current = col;
		while(current < SEATS_PER_ROW && seats[row][current] == 0) {
			 count++;
			 current++;
			 if (count == seatsNeeded) {
			 	return min
			 }
		}

		count = 0
		col++;
		min = col;
	}

	return -1;
}















