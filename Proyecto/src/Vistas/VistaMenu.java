package Vistas;

import java.awt.EventQueue;

import javax.swing.JFrame;
import java.awt.Panel;
import java.awt.Color;
import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.JButton;
import javax.swing.ImageIcon;
import javax.swing.SwingConstants;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class VistaMenu {
	private VistaEmpleado vista_empleado;
	private VistaEmpresa vista_empresa;
	private JFrame frame;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					VistaMenu window = new VistaMenu();
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
	public VistaMenu() {
		vista_empleado=new VistaEmpleado();
		vista_empresa=new VistaEmpresa();
		initialize();
	}
	public JFrame getFrame() {
		return frame;
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 465, 456);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		Panel panel_1 = new Panel();
		panel_1.setBackground(new Color(128, 128, 192));
		panel_1.setBounds(0, 0, 449, 91);
		frame.getContentPane().add(panel_1);
		panel_1.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("Menu");
		lblNewLabel.setBackground(new Color(240, 240, 240));
		lblNewLabel.setFont(new Font("Tw Cen MT Condensed Extra Bold", Font.PLAIN, 24));
		lblNewLabel.setForeground(Color.WHITE);
		lblNewLabel.setBounds(42, 11, 60, 59);
		panel_1.add(lblNewLabel);
		
		Panel panel_2 = new Panel();
		panel_2.setBackground(new Color(210, 215, 221));
		panel_2.setBounds(0, 92, 449, 325);
		frame.getContentPane().add(panel_2);
		panel_2.setLayout(null);
		
		JLabel lblNewLabel_1 = new JLabel("New label");
		lblNewLabel_1.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_1.setIcon(new ImageIcon(VistaMenu.class.getResource("/imagenes/logo.png")));
		lblNewLabel_1.setBounds(291, 0, 158, 413);
		panel_2.add(lblNewLabel_1);
		
		JButton btnEmpleado = new JButton("Empleado");
		btnEmpleado.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				frame.dispose();
				vista_empleado.getFrame().setVisible(true);
				
			}
		});
		btnEmpleado.setBounds(39, 44, 116, 23);
		panel_2.add(btnEmpleado);
		
		JButton btnEmpresa = new JButton("Empresa");
		btnEmpresa.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				frame.dispose();
				vista_empresa.getFrame().setVisible(true);
			}
		});
		btnEmpresa.setBounds(39, 108, 116, 23);
		panel_2.add(btnEmpresa);
	}
}
