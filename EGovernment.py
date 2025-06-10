import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class FactorialCalculator extends JFrame {
    private JTextField inputField;
    private JLabel resultLabel;

    public FactorialCalculator() {
        setTitle("Factorial Calculator");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(300, 150);

        initUI();
    }

    private void initUI() {
        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(3, 2));

        JLabel inputLabel = new JLabel("Enter a number:");
        inputField = new JTextField();
        JButton calculateButton = new JButton("Calculate");
        resultLabel = new JLabel();

        calculateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                calculateFactorial();
            }
        });

        panel.add(inputLabel);
        panel.add(inputField);
        panel.add(new JLabel()); // Empty space
        panel.add(calculateButton);
        panel.add(new JLabel()); // Empty space
        panel.add(resultLabel);

        add(panel);

        setVisible(true);
    }

    private void calculateFactorial() {
        try {
            int number = Integer.parseInt(inputField.getText());
            long factorial = 1;

            for (int i = 1; i <= number; i++) {
                factorial *= i;
            }

            resultLabel.setText("Factorial: " + factorial);
        } catch (NumberFormatException ex) {
            resultLabel.setText("Invalid input. Please enter a valid number.");
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new FactorialCalculator();
        });
    }
}