package Vistas;

import java.awt.EventQueue;

import javax.swing.JFrame;
import java.awt.Panel;
import java.awt.Color;
import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JTextField;

import composicion.Empleado;
import composicion.Aplicacion;

import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.awt.event.ActionEvent;

public class VistaEmpleado {
	
	private VistaMenu vista_menu;
	private JFrame frame;
	private final Panel panel = new Panel();
	private JTextField Nombre;
	private JTextField Puesto;
	private JTextField Direccion;
	private JTextField Ciudad;
	private JTextField Numero;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					VistaEmpleado window = new VistaEmpleado();
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
	public VistaEmpleado() {
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
		frame.setBounds(100, 100, 483, 490);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		panel.setBackground(new Color(204, 255, 204));
		panel.setBounds(0, 0, 467, 101);
		frame.getContentPane().add(panel);
		panel.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("Datos de Empleado");
		lblNewLabel.setFont(new Font("Tw Cen MT Condensed Extra Bold", Font.PLAIN, 24));
		lblNewLabel.setBounds(10, 11, 256, 58);
		panel.add(lblNewLabel);
		
		JPanel panel_1 = new JPanel();
		panel_1.setBackground(new Color(255, 255, 204));
		panel_1.setBounds(0, 107, 467, 344);
		frame.getContentPane().add(panel_1);
		panel_1.setLayout(null);
		
		JLabel lblNewLabel_1 = new JLabel("Nombre:");
		lblNewLabel_1.setBounds(40, 33, 83, 14);
		panel_1.add(lblNewLabel_1);
		
		Nombre = new JTextField();
		Nombre.setBounds(149, 30, 236, 20);
		panel_1.add(Nombre);
		Nombre.setColumns(10);
		
		JButton btnAceptar = new JButton("Aceptar");
		btnAceptar.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String nombre= Nombre.getText();
				String puesto= Puesto.getText();
				String ciudad= Ciudad.getText();
				String dir= Direccion.getText();
				int num= Integer.parseInt(Numero.getText());
				Empleado emp= new Empleado(nombre,puesto,ciudad,dir,num);
				Datos.emps.add(emp);
				Datos.empsNoms.add(emp.getNombre());
				
				
			}
		});
		btnAceptar.setBounds(34, 223, 89, 23);
		panel_1.add(btnAceptar);
		
		JButton btnSalir = new JButton("Salir");
		btnSalir.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				frame.dispose();
				vista_menu=new VistaMenu();
				vista_menu.getFrame().setVisible(true);
			}
		});
		btnSalir.setBounds(296, 223, 89, 23);
		panel_1.add(btnSalir);
		
		JLabel lblNewLabel_2 = new JLabel("Puesto:");
		lblNewLabel_2.setBounds(40, 57, 83, 12);
		panel_1.add(lblNewLabel_2);
		
		JLabel lblNewLabel_3 = new JLabel("Direccion:");
		lblNewLabel_3.setBounds(40, 108, 98, 12);
		panel_1.add(lblNewLabel_3);
		
		Puesto = new JTextField();
		Puesto.setBounds(149, 54, 236, 18);
		panel_1.add(Puesto);
		Puesto.setColumns(10);
		
		Direccion = new JTextField();
		Direccion.setColumns(10);
		Direccion.setBounds(149, 105, 236, 18);
		panel_1.add(Direccion);
		
		Ciudad = new JTextField();
		Ciudad.setBounds(149, 82, 236, 18);
		panel_1.add(Ciudad);
		Ciudad.setColumns(10);
		
		Numero = new JTextField();
		Numero.setColumns(10);
		Numero.setBounds(149, 133, 236, 18);
		panel_1.add(Numero);
		
		JLabel lblNewLabel_4 = new JLabel("Ciudad:");
		lblNewLabel_4.setBounds(40, 86, 83, 12);
		panel_1.add(lblNewLabel_4);
		
		JLabel lblNewLabel_5 = new JLabel("Numero:");
		lblNewLabel_5.setBounds(40, 136, 83, 12);
		panel_1.add(lblNewLabel_5);
	}
}

