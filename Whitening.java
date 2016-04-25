import org.apache.commons.math3.linear.Array2DRowRealMatrix;
import org.apache.commons.math3.linear.EigenDecomposition;
import org.apache.commons.math3.linear.RealMatrix;
import org.apache.commons.math3.stat.correlation.Covariance;
import java.util.ArrayList;

/**
 * Created by alex on 15-5-30.
 */
public class Whitening {
    private DataBuilder dataBuilder;

    public Whitening(DataBuilder dataBuilder){
        this.dataBuilder = dataBuilder;
    }

    public void PCAWhitening(ArrayList<ArrayList<Double>> data){
        PreTreatment preTreatment = new PreTreatment(dataBuilder);
        preTreatment.SubstracMean(dataBuilder.getData());
        preTreatment.NormalizeVariance(dataBuilder.getData());

        RealMatrix dataMatrix = new Array2DRowRealMatrix(dataBuilder.getRow(),dataBuilder.getColumn());

        for(int i = 0; i < data.size(); i++){
            for(int j = 0; j < data.get(i).size(); j++){
                dataMatrix.addToEntry(i,j,data.get(i).get(j));
            }
        }

        Covariance covariance = new Covariance(dataMatrix);
        RealMatrix covarianceMatrix = covariance.getCovarianceMatrix();
        EigenDecomposition eigenDecomposition = new EigenDecomposition(covarianceMatrix);
        RealMatrix U = eigenDecomposition.getV();
        double eigenvalues[] = eigenDecomposition.getRealEigenvalues();
        U = U.transpose();
        for(int i = 0; i < dataBuilder.getRow(); i++){
            dataMatrix.setRowVector(i,U.operate(dataMatrix.getRowVector(i)));
        }

        Covariance covariance2 = new Covariance(dataMatrix);
        RealMatrix result = covariance2.getCovarianceMatrix();


        for(int i = 0; i < dataMatrix.getColumnDimension(); i++){

            dataMatrix.setColumnVector(i, dataMatrix.getColumnVector(i).mapDivideToSelf(Math.sqrt(result.getEntry(i, i) + 0.00001)));
        }

        Covariance covariance3 = new Covariance(dataMatrix);
        RealMatrix finalResult = covariance3.getCovarianceMatrix();

        for(int i = 0; i < 100; i++){
            for(int j = 0; j < 100; j++){
                System.out.print(finalResult.getEntry(i, j) + " ");
            }
            System.out.println();
        }
    }

    private RealMatrix[] PCAWhiteningForZCAWhitening(ArrayList<ArrayList<Double>> data){
        PreTreatment preTreatment = new PreTreatment(dataBuilder);
        preTreatment.SubstracMean(dataBuilder.getData());
        preTreatment.NormalizeVariance(dataBuilder.getData());

        RealMatrix dataMatrix = new Array2DRowRealMatrix(dataBuilder.getRow(),dataBuilder.getColumn());


        for(int i = 0; i < data.size(); i++){
            for(int j = 0; j < data.get(i).size(); j++){
                dataMatrix.addToEntry(i,j,data.get(i).get(j));
            }
        }

        Covariance covariance = new Covariance(dataMatrix);
        RealMatrix covarianceMatrix = covariance.getCovarianceMatrix();

        System.out.println("covariance matrix of original data after zero-mean process:");
        for(int i = 0; i < 2; i++){
            for(int j = 0; j < 2; j++){
                System.out.print(covarianceMatrix.getEntry(i,j) + " ");
            }
            System.out.println();
        }

        EigenDecomposition eigenDecomposition = new EigenDecomposition(covarianceMatrix);
        RealMatrix U = eigenDecomposition.getV();
        U = U.transpose();
        for(int i = 0; i < dataBuilder.getRow(); i++){
            dataMatrix.setRowVector(i,U.operate(dataMatrix.getRowVector(i)));
        }

        Covariance covariance2 = new Covariance(dataMatrix);
        RealMatrix result = covariance2.getCovarianceMatrix();


        for(int i = 0; i < dataMatrix.getColumnDimension(); i++){

            dataMatrix.setColumnVector(i, dataMatrix.getColumnVector(i).mapDivideToSelf(Math.sqrt(result.getEntry(i, i) + 0.00001)));
        }

        Covariance covariance3 = new Covariance(dataMatrix);
        RealMatrix finalResult = covariance3.getCovarianceMatrix();

        System.out.println("\nthe covariance matrix of data after PCA whitening:");
        for(int i = 0; i < 2; i++){
            for(int j = 0; j < 2; j++){
                System.out.print(finalResult.getEntry(i, j) + " ");
            }
            System.out.println();
        }
        RealMatrix returnRealMatrix[] = new RealMatrix[2];
        returnRealMatrix[0] = eigenDecomposition.getV();
        returnRealMatrix[1] = dataMatrix;
        return returnRealMatrix;
    }

    public void ZCAWhitening(ArrayList<ArrayList<Double>> data){
        RealMatrix[] uAndDataMatrix = PCAWhiteningForZCAWhitening(data);
        RealMatrix U = uAndDataMatrix[0];
        RealMatrix dataMatrix = uAndDataMatrix[1];
        for(int i = 0; i < dataMatrix.getRowDimension(); i++){
            dataMatrix.setRowVector(i,U.operate(dataMatrix.getRowVector(i)));
        }

        Covariance covariance3 = new Covariance(dataMatrix);
        RealMatrix finalResult = covariance3.getCovarianceMatrix();

        System.out.println("\nthe covariance matrix of data after ZCA whitening:");
        for(int i = 0; i < 2; i++){
            for(int j = 0; j < 2; j++){
                System.out.print(finalResult.getEntry(i,j) + " ");
            }
            System.out.println();
        }
    }
}


