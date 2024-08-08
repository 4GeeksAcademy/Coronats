import React, { useState } from "react";

export const AddAlleries = ({ show, handleClose, handleSubmit, handleChange, formData }) => {
  
    return (
    <Modal show={show} onHide={handleClose}>
      <Modal.Header closeButton>
        <Modal.Title>Añadir alérgeno</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Form>
          <Form.Group controlId="formName">
            <Form.Label>Nombre</Form.Label>
            <Form.Control
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              placeholder="Nombre del alérgeno"
            />
          </Form.Group>
          <Form.Group controlId="formImage">
            <Form.Label>Imagen</Form.Label>
            <Form.Control
              type="text"
              name="img"
              value={formData.img}
              onChange={handleChange}
              placeholder="URL de la imagen"
            />
          </Form.Group>
        </Form>
      </Modal.Body>
      <Modal.Footer>
        <Button variant="secondary" onClick={handleClose}>
          Cancelar
        </Button>
        <Button variant="primary" onClick={handleSubmit}>
          Guardar
        </Button>
      </Modal.Footer>
    </Modal>
  );
};

