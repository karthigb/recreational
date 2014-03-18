import java.util.concurrent.LinkedBlockingDeque;
import java.util.HashSet;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.net.*;
import java.io.*;

public class FlipBoardChallenge {

	public static class Coordinate {

		public int y = 0;
		public int x = 0;
		public boolean up = false;
		public boolean down = false;
		public boolean left = false;
		public boolean right = false;
		public Coordinate founder = null;
		public boolean start = false;
		public boolean end = false;
		public static HashSet<FlipBoardChallenge.Coordinate> known = new HashSet<FlipBoardChallenge.Coordinate>();

		Coordinate(int x, int y, Coordinate founder) {
			this.y = y;
			this.x = x;
			this.setWhoFound(founder);
		}

		Coordinate(int x, int y) {
			this.y = y;
			this.x = x;
		}

		Coordinate() {
		}

		public void setPath(Coordinate adjacent) {
			if (this.x > adjacent.x && this.y == adjacent.y) {
				this.left = true;
				adjacent.right = true;
			} else if (this.x < adjacent.x && this.y == adjacent.y) {
				this.right = true;
				adjacent.left = true;
			} else if (this.y < adjacent.y && this.x == adjacent.x) {
				this.up = true;
				adjacent.down = true;
			} else if (this.y > adjacent.y && this.x == adjacent.x) {
				this.down = true;
				adjacent.up = true;
			}
		}

		public void setPath(boolean up, boolean right, boolean down, boolean left) {
			this.up = up;
			this.right = right;
			this.down = down;
			this.left = left;
		}

		public String drawRepresentation() {
			if (this.start) {
				return "S";
			}
			else if (this.end) {
				return "E";
			}
			else if (this.up && this.right && this.down && this.left) {
				return "╬";
			} else if (this.up && this.down && this.right) {
				return "╠";
			} else if (this.up && this.right && this.left) {
				return "╩";
			} else if (this.up && this.left && this.down) {
				return "╣";
			} else if (this.right && this.down && this.left) {
				return "╦";
			} else if (this.up && this.left) {
				return "╝";
			} else if (this.up && this.down) {
				return "║";
			} else if (this.up && this.right) {
				return "╚";
			} else if (this.right && this.left) {
				return "═";
			} else if (this.down && this.left) {
				return "╗";
			} else if (this.right && this.down) {
				return "╔";
			} else if (this.up) {
				return "╨";
			} else if (this.left) {
				return "╡";
			} else if (this.down) {
				return "╥";
			} else if (this.right) {
				return "╞";
			} else {
				return "?";
			}
		}
		
		@Override
		public int hashCode() {
			return (31 * (31 * this.x) + this.y);
		}

		@Override
		public boolean equals(Object other) {
			if (!(other instanceof Coordinate)) {
				return false;
			}
			Coordinate point = (Coordinate) other;
			return this.y == point.y && this.x == point.x;
		}
		
		public void setWhoFound(Coordinate founder) {
			this.setPath((this.founder = founder));
		}

		public String toString() {
			return String.format("(%d, %d)", this.x, this.y);
		}
	}

	static LinkedBlockingDeque<FlipBoardChallenge.Coordinate> orderToCheck = new LinkedBlockingDeque<FlipBoardChallenge.Coordinate>();
	static String session;
	static int maxX = 0;
	static int maxY = 0;
	static int minX = 0;
	static int minY = 0;

	public static Coordinate nextToCheck() {
		return orderToCheck.poll();
	}

	public static void addToQueue(Coordinate loc) {
		if (!Coordinate.known.contains(loc)) {
			Coordinate.known.add(loc);
			maxX = loc.x > maxX ? loc.x : maxX;
			maxY = loc.y > maxY ? loc.y : maxY;
			minX = loc.y < minX ? loc.x : minX;
			minY = loc.y < minY ? loc.y : minY;
			orderToCheck.add(loc);
		}
	}

	public static void surveyCoordinate(String text, Coordinate current) {
		Matcher m = Pattern.compile("\\(\\s*+(-?+\\d+)\\s*+,\\s*+(-?+\\d+)\\s*+\\)").matcher(text);
		while (m.find()) {
			int x = Integer.parseInt(m.group(1));
			int y = Integer.parseInt(m.group(2));
			addToQueue(new Coordinate(x, y, current));
		}
	}

	public static void traverseMaze() {
		Coordinate current;
		while ((current = nextToCheck()) instanceof Coordinate) {
			try {
				String content = getPageContent(buildUrl(current));
				if (exitFound(content)) {
					current.end = true;
					drawRepresentation();
					System.out.println(showAnswer(current));
				} else {
					surveyCoordinate(content, current);
				}
			} catch (Exception e) {
				System.out.println(e);
				System.exit(1);
			}
		}
	}

	public static String buildUrl(Coordinate current){
		return String.format("https://challenge.flipboard.com/m?s=%s&x=%d&y=%d", session, current.x, current.y);
	}

	public static boolean exitFound(String content) {
		Matcher m = Pattern.compile("\\bend:true").matcher(content);
		if (m.find()) {
			return true;
		}
		if (content.contains("true")) {
			System.out.println(content);
		}
		return false;
	}

	public static String getPageContent(String url) throws Exception {
		URL challengeURL = new URL(url);
		BufferedReader in = new BufferedReader(new InputStreamReader(challengeURL.openStream()));

		String inputLine;
		while ((inputLine = in.readLine()) != null && !inputLine.contains("end"));
		in.close();
		return inputLine;
	}

	public static String showAnswer(Coordinate loc) {
		if (loc.founder instanceof Coordinate) { 
			return String.format("%s, %s", showAnswer(loc.founder), loc);
		}
		return loc.toString();
	}
	
	public static void drawRepresentation() {
		int xLength = maxX - minX + 1;
		int yLength = maxY - minY + 1;
		String[][] maze = new String[yLength][xLength];
		for (int x = 0; x < xLength; x++)
			for (int y = 0; y < yLength; y++)
				maze[y][x] = "?";
		for (Coordinate loc : Coordinate.known)
			maze[yLength - loc.y - 1][loc.x] = loc.drawRepresentation(); 
		for (int y = 0; y < xLength; y++) {
			for (int x = 0; x < xLength; x++)
				System.out.print(maze[y][x]);
			System.out.println("");
		}
	}
	
	public static void main(String[] arg) {
		if (arg.length > 1) {
			session = arg[1];
		}
		else {
			session = "4621977949848877596.32";
		}
		Coordinate start = new Coordinate(0, 0);
		start.start = true;
		addToQueue(start);
		traverseMaze();
	}
}
