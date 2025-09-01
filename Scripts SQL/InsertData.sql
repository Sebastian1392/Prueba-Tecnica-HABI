-- Insertar los estados base
INSERT INTO status (name) VALUES
('en_venta'),
('pre_venta'),
('vendido'),
('deshabilitado'); -- Este estado no debería aparecer en los resultados

-- Insertar las propiedades
INSERT INTO property (address, city, price, description, year) VALUES
('Calle 123 #45-67', 'bogota', 350000000.00, 'Apartamento con excelente vista', 2020),
('Avenida Siempre Viva 742', 'medellin', 480000000.00, 'Casa amplia con patio', 2011),
('Carrera 7 #89-10', 'bogota', 280000000.00, 'Apartaestudio moderno y céntrico', 2022),
('Diagonal 45 #12-34', 'cali', 210000000.00, 'Apartamento remodelado', 2015);

-- Insertar el historial de estados para crear una "historia"
-- Inmueble 1: Su último estado es 'en_venta'
INSERT INTO status_history (property_id, status_id, update_date) VALUES
(1, 2, '2025-08-29 10:00:00'), -- pre_venta
(1, 1, '2025-08-30 11:00:00'); -- en_venta (el más reciente)

-- Inmueble 2: Su último estado es 'vendido'
INSERT INTO status_history (property_id, status_id, update_date) VALUES
(2, 1, '2025-08-20 15:00:00'), -- en_venta
(2, 3, '2025-08-28 18:00:00'); -- vendido (el más reciente)

-- Inmueble 3: Su último estado es 'pre_venta'
INSERT INTO status_history (property_id, status_id, update_date) VALUES
(3, 2, '2025-08-30 09:00:00'); -- pre_venta (el más reciente)

-- Inmueble 4: Su último estado es 'deshabilitado' (no debe aparecer)
INSERT INTO status_history (property_id, status_id, update_date) VALUES
(4, 1, '2025-07-15 12:00:00'), -- en_venta
(4, 4, '2025-08-25 14:00:00'); -- deshabilitado (el más reciente)