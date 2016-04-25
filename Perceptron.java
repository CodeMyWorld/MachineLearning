import java.util.ArrayList;

/**
 * Created by alex on 15-5-27.
 */
public class Perceptron {

    private DataBuilder dataBuilder;
    private ArrayList<Double> weights;
    private double bias;

    public Perceptron(DataBuilder dataBuilder){
        this.dataBuilder = dataBuilder;
        weights = new ArrayList<>();
        for(int i = 0; i < dataBuilder.getColumn(); i++){
            weights.add(1.0);
        }
    }

    public void perceptronTrain(int iteration){
        for(int i = 0; i < iteration; i++){
            if(activeFunction(dot_product(dataBuilder.getData().get(i),weights) + bias) !=
                    dataBuilder.getLabels().get(i)){
                for(int j = 0; j < dataBuilder.getColumn(); j++){
                    weights.set(j,Arith.add(weights.get(j) ,
                            0.5*dataBuilder.getLabels().get(i) * dataBuilder.getData().get(i).get(j)));
                    bias += dataBuilder.getLabels().get(i)*0.2;
                }
            }
        }
    }

    public ArrayList<Double> perceptronTrain(int testGroup, int numsOfEachGroup, int[][] group) {
        ArrayList<Double> weightsList = new ArrayList<>();
        for(int i = 0; i < dataBuilder.getColumn(); i++){
            weightsList.add(0.0);
        }
        for (int i = 0; i < group.length; i++) {
            if (i != testGroup) {
                for (int k = 0; k < numsOfEachGroup; k++) {
                    if (activeFunction(dot_product(dataBuilder.getData().get(group[i][k]), weightsList)+bias) !=
                            dataBuilder.getLabels().get(group[i][k])) {
                        for (int j = 0; j < dataBuilder.getColumn(); j++) {
                            weightsList.set(j, Arith.add(weightsList.get(j),
                                    0.2*dataBuilder.getLabels().get(group[i][k]) * dataBuilder.getData().get(group[i][k]).get(j)));
                            bias += dataBuilder.getLabels().get(group[i][k])*0.2;
                        }
                    }
                }
            }
        }
        return weightsList;
    }

    public double dot_product(ArrayList<Double>dataRow, ArrayList<Double>weights){
        double result = 0;
        for(int i = 0; i < dataBuilder.getColumn(); i++){
            result = Arith.add(result,Arith.mul(dataRow.get(i),weights.get(i)));
        }
        //System.out.println(result);
        return result;
    }

    public int activeFunction(double n){
        if(n >= 0){
            return 1;
        }
        else{
            return -1;
        }
    }
    public double getBias() {
        return bias;
    }

    public void setBias(double bias) {
        this.bias = bias;
    }

    public void showWeights(){
        for(int i = 0; i < weights.size(); i++){
            System.out.println(weights.get(i));
        }
    }
}
