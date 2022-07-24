import javax.swing.JOptionPane;
// import java.lang.*;

class FinalProjectComProgSourceCodeDebug1 {
    public static void main(String[] args)
    {
String[] question = {"Future Worth", "Present Worth", "Interest Rate", "N-Years"};
        int x = JOptionPane.showOptionDialog(null, "What to find?", "Compound Interest", JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, question, question[0]);

        if (x == 0) {
            futureWorth();
        } else if (x == 1) {
            presentWorth();
        } else if (x == 2) {
            intRate();
        } else{
            nYears();
    }
    }
    public static void futureWorth() {
        String pWorth = JOptionPane.showInputDialog("Enter Present Worth: ");
        while (((pWorth.matches("[.-9]+") && pWorth.length() >= 1) == false) || Float.parseFloat(pWorth)<=0) {
            pWorth = JOptionPane.showInputDialog("Invalid value. Enter Present Worth: ");
        }

        String interestRate = JOptionPane.showInputDialog("Enter Interest Rate in %: ");
        while (((interestRate.matches("[.-9]+") && interestRate.length() >= 1) == false) || Float.parseFloat(interestRate)<=0) {
            interestRate = JOptionPane.showInputDialog("Invalid value. Enter Interest Rate in %: ");
        }
        String years = JOptionPane.showInputDialog("Enter N-years: ");
        while (((years.matches("[.-9]+") && years.length() >= 1) == false) || Float.parseFloat(years)<=0) {
            years = JOptionPane.showInputDialog("Invalid value. Enter N-years: ");
        }
        String[] comPeriod = {"Annually", "Semi-Annually", "Quarterly", "Monthly"};
        int tempm = JOptionPane.showOptionDialog(null, "Choose Compounding Period.", "Compound Interest", JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, comPeriod, comPeriod[0]);

        String compound;
        float m;
        if (tempm == 0) {
            m = 1;
            compound = comPeriod[0];
        } else if (tempm == 1) {
            m = 2;
            compound = comPeriod[1];
        } else if (tempm == 2) {
            m = 4;
            compound = comPeriod[2];
        } else {
            m = 12;
            compound = comPeriod[3];
        }

        float p = Float.parseFloat(pWorth);
        float i = Float.parseFloat(interestRate) / 100;
        float n = Float.parseFloat(years) * m;

        float finalvalue = (float) (p * Math.pow(1 + (i / m), n));
        String message = "The Future Worth of " + p + " at an Interest rate of " + interestRate + " % compounded " + compound + " in " + years + " years is " + String.format("%.2f", finalvalue) ;
        JOptionPane.showMessageDialog(null, message);
    }

    public static void presentWorth() {
        String fWorth = JOptionPane.showInputDialog("Enter Future Worth: ");
        while (((fWorth.matches("[.-9]+") && fWorth.length() >= 1) == false) || Float.parseFloat(fWorth)<=0) {
            fWorth = JOptionPane.showInputDialog("Invalid value. Enter Future Worth: ");
        }

        String interestRate = JOptionPane.showInputDialog("Enter Interest Rate in %: ");
        while (((interestRate.matches("[.-9]+") && interestRate.length() >= 1) == false) || Float.parseFloat(interestRate)<=0) {
            interestRate = JOptionPane.showInputDialog("Invalid value. Enter Interest Rate in %: ");
        }
        String years = JOptionPane.showInputDialog("Enter N-years: ");
        while (((years.matches("[.-9]+") && years.length() >= 1) == false) || Float.parseFloat(years)<=0) {
            years = JOptionPane.showInputDialog("Invalid value. Enter N-years: ");
        }
        String[] comPeriod = {"Annually", "Semi-Annually", "Quarterly", "Monthly"};
        int tempm = JOptionPane.showOptionDialog(null, "Choose Compounding Period.", "Compound Interest", JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, comPeriod, comPeriod[0]);

        String compound;
        float m;
        if (tempm == 0) {
            m = 1;
            compound = comPeriod[0];
        } else if (tempm == 1) {
            m = 2;
            compound = comPeriod[1];
        } else if (tempm == 2) {
            m = 4;
            compound = comPeriod[2];
        } else {
            m = 12;
            compound = comPeriod[3];
        }

        float f = Float.parseFloat(fWorth);
        float i = Float.parseFloat(interestRate) / 100;
        float n = Float.parseFloat(years) * m;

        float finalvalue = (float) (f * Math.pow(1 + (i / m), -n));
        String message = "The Present Worth of " + f + " at an interst rate of "+ interestRate + " % compounded " + compound + " in " + years + " years is " + String.format("%.2f", finalvalue);
        JOptionPane.showMessageDialog(null, message);
    }
    public static void intRate() {
        String pWorth = JOptionPane.showInputDialog("Enter Present Worth: ");
        while (((pWorth.matches("[.-9]+") && pWorth.length() >= 1) == false) || Float.parseFloat(pWorth)<=0) {
            pWorth = JOptionPane.showInputDialog("Invalid value. Enter Present Worth: ");
        }
        String fWorth = JOptionPane.showInputDialog("Enter Future Worth: ");
        while (((fWorth.matches("[.-9]+") && fWorth.length() >= 1) == false) || Float.parseFloat(fWorth)<=0) {
            fWorth = JOptionPane.showInputDialog("Invalid value. Enter Future Worth: ");
        }
        while (Float.parseFloat(fWorth) < Float.parseFloat(pWorth)){
            String message = "Future Worth can not be less than Present Worth.";
            JOptionPane.showMessageDialog(null, message);
            pWorth = JOptionPane.showInputDialog("Enter Present Worth: ");
            while (((pWorth.matches("[.-9]+") && pWorth.length() >= 1) == false) || Float.parseFloat(pWorth)<=0) {
                pWorth = JOptionPane.showInputDialog("Invalid value. Enter Present Worth: ");
            }
            fWorth = JOptionPane.showInputDialog("Enter Future Worth: ");
            while (((fWorth.matches("[.-9]+") && fWorth.length() >= 1) == false) || Float.parseFloat(fWorth)<=0) {
                fWorth = JOptionPane.showInputDialog("Invalid value. Enter Future Worth: ");
            }
        }
        String years = JOptionPane.showInputDialog("Enter N-years: ");
        while (((years.matches("[.-9]+") && years.length() >= 1) == false) || Float.parseFloat(years)<=0) {
            years = JOptionPane.showInputDialog("Invalid value. Enter N-years: ");
        }

        String[] comPeriod = {"Annually", "Semi-Annually", "Quarterly", "Monthly"};
        int tempm = JOptionPane.showOptionDialog(null, "Choose Compounding Period.", "Compound Interest", JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, comPeriod, comPeriod[0]);
        String compound;
        float m;
        if (tempm == 0) {
            m = 1;
            compound = comPeriod[0];
        } else if (tempm == 1) {
            m = 2;
            compound = comPeriod[1];
        } else if (tempm == 2) {
            m = 4;
            compound = comPeriod[2];
        } else {
            m = 12;
            compound = comPeriod[3];
        }

        float f = Float.parseFloat(fWorth);
        float p = Float.parseFloat(pWorth);
        float n = Float.parseFloat(years)*m;

        float finalvalue = (float) (m*(Math.pow(f/p,1/n)-1));
        String message = "The Interest Rate of a money with Present Worth of " + p + " and Future Worth of " + f + " with an interest Compounded " + compound + " in " + years + " years " + " is " + String.format("%.2f", finalvalue*100) + "%";
        JOptionPane.showMessageDialog(null, message);
    }
    public static void nYears() {
        String pWorth = JOptionPane.showInputDialog("Enter Present Worth: ");
        while (((pWorth.matches("[.-9]+") && pWorth.length() >= 1) == false) || Float.parseFloat(pWorth)<=0) {
            pWorth = JOptionPane.showInputDialog("Invalid value. Enter Present Worth: ");
        }
        String fWorth = JOptionPane.showInputDialog("Enter Future Worth: ");
        while (((fWorth.matches("[.-9]+") && fWorth.length() >= 1) == false) || Float.parseFloat(fWorth)<=0) {
            fWorth = JOptionPane.showInputDialog("Invalid value. Enter Future Worth: ");
        }
        while (Float.parseFloat(fWorth) < Float.parseFloat(pWorth)){
            String message = "Future Worth can not be less than Present Worth.";
            JOptionPane.showMessageDialog(null, message);
            pWorth = JOptionPane.showInputDialog("Enter Present Worth: ");
            while (((pWorth.matches("[.-9]+") && pWorth.length() >= 1) == false) ||  Float.parseFloat(pWorth)<=0) {
                pWorth = JOptionPane.showInputDialog("Invalid value. Enter Present Worth: ");
            }
            fWorth = JOptionPane.showInputDialog("Enter Future Worth: ");
            while (((fWorth.matches("[.-9]+") && fWorth.length() >= 1) == false) || Float.parseFloat(fWorth)<=0) {
                fWorth = JOptionPane.showInputDialog("Invalid value. Enter Future Worth: ");
            }
        }
        String interestRate = JOptionPane.showInputDialog("Enter Interest Rate in %: ");
        while (((interestRate.matches("[.-9]+") && interestRate.length() >= 1) == false) || Float.parseFloat(interestRate) <= 0) {
            interestRate = JOptionPane.showInputDialog("Invalid value. Enter Interest Rate in %: ");
        }
        String[] comPeriod = {"Annually", "Semi-Annually", "Quarterly", "Monthly"};
        int tempm = JOptionPane.showOptionDialog(null, "Choose Compounding Period.", "Compound Interest", JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, comPeriod, comPeriod[0]);
        String compound;
        float m;
        if (tempm == 0) {
            m = 1;
            compound = comPeriod[0];
        } else if (tempm == 1) {
            m = 2;
            compound = comPeriod[1];
        } else if (tempm == 2) {
            m = 4;
            compound = comPeriod[2];
        } else {
            m = 12;
            compound = comPeriod[3];
        }

        float f = Float.parseFloat(fWorth);
        float p = Float.parseFloat(pWorth);
        float i = Float.parseFloat(interestRate)/100;

        float assertEquals = (float) (customLog((float)(1+(i/m)), f/p))/m;
        String message = "It will take " + String.format("%.1f", assertEquals) + " years for a money amounting " + p + " to have a Future Worth of " + f + " if it is compounded " + compound + " at an interest rate of " + interestRate + "%";
        JOptionPane.showMessageDialog(null, message);

    }
    public static double customLog(double base, double logNumber) {
        return Math.log(logNumber) / Math.log(base);}}