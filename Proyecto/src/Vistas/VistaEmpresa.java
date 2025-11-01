package Vistas;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.BorderLayout;
import java.awt.Color;
import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.JTextField;

import composicion.Empleado;
import composicion.Empresa;

import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.awt.event.ActionEvent;

public class VistaEmpresa {
	private VistaLista vista_lista;
	private VistaMenu vista_menu;
	private JFrame frame;
	private JTextField Nombre;
	

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					VistaEmpresa window = new VistaEmpresa();
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
	public VistaEmpresa() {
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
		frame.setBounds(100, 100, 590, 543);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		JPanel panel = new JPanel();
		panel.setBackground(new Color(64, 128, 128));
		panel.setBounds(0, 0, 576, 78);
		frame.getContentPane().add(panel);
		panel.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("Empresa");
		lblNewLabel.setFont(new Font("Segoe UI Semibold", Font.PLAIN, 36));
		lblNewLabel.setForeground(new Color(255, 255, 255));
		lblNewLabel.setBackground(new Color(255, 255, 255));
		lblNewLabel.setBounds(31, 10, 397, 34);
		panel.add(lblNewLabel);
		
		JPanel panel_1 = new JPanel();
		panel_1.setBackground(new Color(214, 228, 211));
		panel_1.setBounds(0, 78, 576, 428);
		frame.getContentPane().add(panel_1);
		panel_1.setLayout(null);
		
		JLabel lblNewLabel_1 = new JLabel("Nombre:");
		lblNewLabel_1.setBounds(53, 41, 160, 27);
		panel_1.add(lblNewLabel_1);
		
		JLabel lbError = new JLabel("");
		lbError.setBounds(199, 164, 160, 20);
		panel_1.add(lbError);
		
		Nombre = new JTextField();
		Nombre.setBounds(217, 45, 288, 23);
		panel_1.add(Nombre);
		Nombre.setColumns(10);
		
		JButton btnNewButton = new JButton("Aceptar");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String nombre= Nombre.getText();
				if(nombre.isEmpty()) {
					lbError.setText("Escriba un nombre válido");
				}else {
					Empresa empr=new Empresa(nombre);
					Datos.Empr.add(empr);
				}
				
			}
		});
		btnNewButton.setBounds(37, 209, 84, 20);
		panel_1.add(btnNewButton);
		
		JButton btnNewButton_1 = new JButton("Contratar");
		btnNewButton_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String nombre= Nombre.getText();
			    for (int i = 0; i < Datos.Empr.size(); i++) {
			        if (Datos.Empr.get(i).getNombre().equalsIgnoreCase(nombre)) {
			        	Datos.indice=i;
			        	break;
			        }
			    }
			    if (Datos.indice==-1) {
			    	lbError.setText("Escriba un nombre válido");
			    }else {
			    	frame.dispose();
				    vista_lista=new VistaLista();
				    vista_lista.getFrame().setVisible(true);
			    	
			    }
			    
				
				
			}
		});
		btnNewButton_1.setBounds(217, 209, 130, 20);
		panel_1.add(btnNewButton_1);
		
		JButton btnNewButton_2 = new JButton("Salir");
		btnNewButton_2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				frame.dispose();
				vista_menu=new VistaMenu();
				vista_menu.getFrame().setVisible(true);
				
			}
		});
		btnNewButton_2.setBounds(421, 209, 84, 20);
		panel_1.add(btnNewButton_2);
		

	}
}
