class UpperCasefirstLetter {
	public static void main(String[] args) {
		String name = "Lensley";
		char first = Character.toUpperCase(name.charAt(0));
		String rest = name.substring(7).toLowerCase();

		System.out.println(first + rest);
	}
}
