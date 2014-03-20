package Flipboard;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class MazeSolver {
	
	private String mazeUrl = "https://challenge.flipboard.com/m?s=1687184559264975024.33";
	private Queue<String[]> notInvestigated;
	private Map<String,Boolean> investigated;
	private Map<String[],Queue<String[]>> routes;
	
	MazeSolver() throws MalformedURLException{
		notInvestigated = new LinkedList<String[]>();
		investigated = new HashMap<String,Boolean>();
		routes = new HashMap<String[],Queue<String[]>>();
	}
		
	private String nextMove(String x, String y) throws Exception {
		URL urlObj = new URL(mazeUrl + "&x=" + x + "&y=" + y);
		HttpURLConnection con = (HttpURLConnection) urlObj.openConnection();
  
		BufferedReader bufferIn = new BufferedReader(
		        new InputStreamReader(con.getInputStream()));
		String inputLine;
		StringBuffer response = new StringBuffer();
 
		while ((inputLine = bufferIn.readLine()) != null) {
			response.append(inputLine);
		}
		bufferIn.close();
		return response.toString(); 
	}

	private List<String[]> getCoordinates(String response) {
		List<String[]> coordList = new LinkedList<String[]>();
        Pattern pattern = Pattern.compile("[0-9]+,[0-9]+");       
        Matcher matcher = pattern.matcher(response);
        while (matcher.find()) {
        	String[] coords = matcher.group().split(",");
        	coordList.add(coords);
        }
        return coordList;
	}
	
	private Queue<String[]> getNewPath(String[] currentPos, String[] coord){
		Queue<String[]> oldPath = routes.get(currentPos);
		Queue<String[]> newPath = new LinkedList<String[]>();
		Iterator<String[]> i = oldPath.iterator();
		while(i.hasNext()){
			newPath.add(i.next());
		}
		newPath.add(coord);
		return newPath;
	}
	
	private void printShortestPath(Queue<String[]> shortestPath){
		Iterator<String[]> i = shortestPath.iterator();
		System.out.println("SHORTEST PATH:");
		while(i.hasNext()){
			String[] coord = i.next();
			System.out.println(coord[0]+","+coord[1]);
		}
	}
	
	private Queue<String[]> startBFS() throws Exception{
		boolean foundExit = false;
		
		//Add starting point to route map
		String[] a = new String[]{"0","0"};
		notInvestigated.add(a);
		Queue<String[]> path = new LinkedList<String[]>();
		path.add(a);
		routes.put(a, path);
		//
		
		String[] currentPos = null;
		System.out.println("EXPLORING:");
		while(!foundExit){
			
			//Dequeue current node
			currentPos = notInvestigated.remove();
			System.out.println(currentPos[0] + "," + currentPos[1]);			
			investigated.put(currentPos[0] + ","+ currentPos[1], true);
			
			//Get connected nodes
			String response = nextMove(currentPos[0],currentPos[1]);
			if(response.contains("true")){
				foundExit=true;
			} else {
				List<String[]> newCoords = getCoordinates(response);
				for(String[] coord: newCoords){
					//Enqueue new coordinates if not already found
					if(!investigated.containsKey(coord[0] + ","+ coord[1])){
						notInvestigated.add(coord);
						//Record path to current coordinate
						routes.put(coord, getNewPath(currentPos,coord));
					}
				}				
			}
		}
		//Found exit - return shortest path
		System.out.println("FOUND EXIT AT COORDINATE: " + currentPos[0] + "," + currentPos[1] + "\n");		
		return routes.get(currentPos);
	}
	
	public static void main(String[] args) throws Exception{
		MazeSolver m = new MazeSolver();
		Queue<String[]> solution = m.startBFS();
		m.printShortestPath(solution);
	}
