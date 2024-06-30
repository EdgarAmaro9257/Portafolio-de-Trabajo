/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package cajeroautomatico;

/**
 *
 * @author edgar
 */
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CajeroAutomatico {

    private static double saldo = 1000.00;

    public static void main(String[] args) {
        // Crear el marco principal
        JFrame frame = new JFrame("Cajero Automático");
        frame.setSize(400, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(null);

        // Crear etiquetas y botones
        JLabel label = new JLabel("Seleccione una operación:");
        label.setBounds(120, 20, 200, 30);
        frame.add(label);

        JButton saldoButton = new JButton("Consultar Saldo");
        saldoButton.setBounds(120, 60, 160, 30);
        frame.add(saldoButton);

        JButton depositarButton = new JButton("Depositar Dinero");
        depositarButton.setBounds(120, 100, 160, 30);
        frame.add(depositarButton);

        JButton retirarButton = new JButton("Retirar Dinero");
        retirarButton.setBounds(120, 140, 160, 30);
        frame.add(retirarButton);

        // Acción para consultar saldo
        saldoButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JOptionPane.showMessageDialog(frame, "Su saldo es: $" + saldo);
            }
        });

        // Acción para depositar dinero
        depositarButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String input = JOptionPane.showInputDialog(frame, "Ingrese la cantidad a depositar:");
                try {
                    double cantidad = Double.parseDouble(input);
                    if (cantidad > 0) {
                        saldo += cantidad;
                        JOptionPane.showMessageDialog(frame, "Depósito exitoso. Su nuevo saldo es: $" + saldo);
                    } else {
                        JOptionPane.showMessageDialog(frame, "Ingrese una cantidad válida.");
                    }
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(frame, "Ingrese una cantidad válida.");
                }
            }
        });

        // Acción para retirar dinero
        retirarButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String input = JOptionPane.showInputDialog(frame, "Ingrese la cantidad a retirar:");
                try {
                    double cantidad = Double.parseDouble(input);
                    if (cantidad > 0 && cantidad <= saldo) {
                        saldo -= cantidad;
                        JOptionPane.showMessageDialog(frame, "Retiro exitoso. Su nuevo saldo es: $" + saldo);
                    } else {
                        JOptionPane.showMessageDialog(frame, "Fondos insuficientes o cantidad no válida.");
                    }
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(frame, "Ingrese una cantidad válida.");
                }
            }
        });

        // Hacer visible el marco
        frame.setVisible(true);
    }
}

