package autoclick;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JTextField;
import java.awt.BorderLayout;
import javax.swing.JButton;
import javax.swing.JLabel;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class clickform {

	private JFrame frame;
	private JTextField textField;
	private JLabel labelrate;
	private double cRate;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					clickform window = new clickform();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public clickform() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 450, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		labelrate = new JLabel("0");
		labelrate.setBounds(247, 87, 100, 15);
		frame.getContentPane().add(labelrate);
		
		
		JButton btnApply = new JButton("Apply");
		btnApply.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				int holder = 0;
				labelrate.setText(textField.getText());
				holder = Integer.valueOf(textField.getText());
				cRate = 1 / holder;
				textField.setText("");
				return;
			}
		});
		btnApply.setBounds(237, 202, 117, 25);
		frame.getContentPane().add(btnApply);
		
		textField = new JTextField();
		textField.setBounds(237, 135, 117, 25);
		frame.getContentPane().add(textField);
		textField.setColumns(10);
		
		JLabel lblFrequencyOfClick = new JLabel("Frequency of Click");
		lblFrequencyOfClick.setBounds(237, 19, 168, 48);
		frame.getContentPane().add(lblFrequencyOfClick);
		
		JLabel lblAutoclicker = new JLabel("AutoClicker");
		lblAutoclicker.setBounds(25, 12, 116, 63);
		frame.getContentPane().add(lblAutoclicker);
		
		JLabel lblCurrentRate = new JLabel("Current Rate:");
		lblCurrentRate.setBounds(25, 66, 117, 57);
		frame.getContentPane().add(lblCurrentRate);
		
		JLabel lblNewRate = new JLabel("New Rate:");
		lblNewRate.setBounds(25, 121, 133, 52);
		frame.getContentPane().add(lblNewRate);
	}
}
