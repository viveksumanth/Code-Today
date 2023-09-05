import java.util.*;

public class ClosestPoints implements Comparable<ClosestPoints> {
    private int[] point;
    private Double distance;
    
    ClosestPoints(int[] point, Double distance) {
        this.point = point;
        this.distance = distance;
    }
    
    @Override
    public int compareTo(ClosestPoints nextPointDistance) {
        if (this.distance > nextPointDistance.distance) {
            return 1;
        }
        else if (this.distance == nextPointDistance.distance) {
            return 0;
        } 
        return -1;
    }
    
    public int[] getPoint() {
        return this.point;
    }
    
    public Double getDistance() {
        return this.distance;
    }
}

class Solution {
    public int[][] kClosest(int[][] points, int k) {

        List<ClosestPoints> distancePoints = new ArrayList<>();
        
        for (int[] eachPoint: points) {
            Integer xi = eachPoint[0];
            Integer yi = eachPoint[1];
            Double distance = Math.sqrt((xi*xi) + (yi*yi));
            distancePoints.add(new ClosestPoints(eachPoint, distance));
        }
        Collections.sort(distancePoints);
        
        int[][] allPoints = new int[distancePoints.size()][];
        int rowIndex = 0;

        for (ClosestPoints point : distancePoints) {
            int[] dataPoint = point.getPoint();
            allPoints[rowIndex] = new int[dataPoint.length];

            for (int i = 0; i < dataPoint.length; i++) {
                allPoints[rowIndex][i] = dataPoint[i];
            }

            rowIndex++;
        }
        int[][] result = Arrays.copyOfRange(allPoints, 0, k);
        return result;
    }
    
}