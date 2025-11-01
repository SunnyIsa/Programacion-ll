package Vistas;

import java.awt.EventQueue;

import javax.swing.JFrame;
import java.awt.FlowLayout;
import java.awt.Window;

import javax.swing.JPanel;
import javax.swing.JList;
import javax.swing.JScrollPane;

import Vistas.VistaEmpleado;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JLabel;

public class VistaLista {
	private VistaEmpresa vista_empresa;
	private JFrame frame;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					VistaLista window = new VistaLista();
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
	public VistaLista() {
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
		frame.setBounds(100, 100, 592, 515);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		JPanel panel = new JPanel();
		panel.setBounds(0, 0, 578, 478);
		frame.getContentPane().add(panel);
		panel.setLayout(null);
		
		JScrollPane scrollPane = new JScrollPane();
		scrollPane.setBounds(284, 39, 229, 362);
		panel.add(scrollPane);
		
		JList empsLista = new JList();
		scrollPane.setViewportView(empsLista);
		empsLista.setListData(Datos.empsNoms.toArray(new String[0]));
		
		JScrollPane scrollPane_1 = new JScrollPane();
		scrollPane_1.setBounds(30, 39, 229, 362);
		panel.add(scrollPane_1);
		
		JList empsCon = new JList();
		scrollPane_1.setViewportView(empsCon);
		empsCon.setListData(Datos.Empr.get(Datos.indice).empsCon.toArray(new String[0]));
		
		JButton btnSalir = new JButton("Salir");
		btnSalir.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				frame.dispose();
				vista_empresa=new VistaEmpresa();
				vista_empresa.getFrame().setVisible(true);
				
			}
		});
		btnSalir.setBounds(463, 437, 84, 20);
		panel.add(btnSalir);
		
		JLabel lblNewLabel = new JLabel("Empleados contratados:");
		lblNewLabel.setBounds(30, 10, 196, 19);
		panel.add(lblNewLabel);
		
		JLabel lblNewLabel_1 = new JLabel("Empleados no contratados:");
		lblNewLabel_1.setBounds(284, 13, 196, 16);
		panel.add(lblNewLabel_1);
		
		JButton btnNewButton = new JButton("Contratar");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String e1=(String) empsLista.getSelectedValue();
				Datos.Empr.get(Datos.indice).empsCon.add(e1);
				for (int i = 0; i < Datos.emps.size(); i++) {
			        if (Datos.emps.get(i).getNombre().equalsIgnoreCase(e1)) {
			        	Datos.Empr.get(Datos.indice).contratar(Datos.emps.get(i));
			        	Datos.emps.remove(Datos.emps.get(i));
			        }
			        }
				Datos.empsNoms.remove(e1);

				empsLista.setListData(Datos.empsNoms.toArray(new String[0]));
				empsCon.setListData(Datos.Empr.get(Datos.indice).empsCon.toArray(new String[0]));
			}
		});
		btnNewButton.setBounds(221, 437, 102, 20);
		panel.add(btnNewButton);
	}
}
