class ParkingLot {

    public static void main(String[] args) {

        String[] parkingLot = {
            "motorcycle",
            "",
            "truck",
            "car",
            "car"
        };

        System.out.println(parkingLot[0]);
        System.out.println(parkingLot[1]);
        System.out.println(parkingLot[2]);
        System.out.println(parkingLot[3]);
        System.out.println(parkingLot[4]);

        // A car enters the empty parking spot
        parkingLot[1] = "car";

        System.out.println("Spot 1 now contains:");
        System.out.println(parkingLot[1]);
    }
}
