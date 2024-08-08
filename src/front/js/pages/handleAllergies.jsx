import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";

export const HandleAllergies = () => {
    const {store, actions} = useContext(Context);
    const [viewProducts, setViewProducts] = useState({});
    const [formData, setFormData] = useState({
        name: "",
        img: "",
    });
    const [showModal, setShowModal] = useState(false);
    const [isEditMode, setIsEditMode] = useState(false);
    const [currentAllergyId, setCurrentAllergyId] = useState(null);

    const toggleExpand = (index) => {
        setViewProducts(prevState => ({
            ...prevState, 
            [index]: !prevState[index],
        }));
    };

    const handleSubmit = () => {
        if (isEditMode) {
            console.log("Editing allergy...", formData);
            actions.editAllergies(formData, currentAllergyId);
        } else {
            console.log("Saving new allergy...", formData);
            actions.addAllergies(formData);
        }
        // Close modal and reset form
        setShowModal(false);
        setIsEditMode(false);
        setFormData({
            name: "",
            img: "",
        });
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value 
        }));
    };

    const handleShowModal = () => {
        setFormData({
            name: "",
            img: "",
        });
        setIsEditMode(false);
        setShowModal(true);
    };

    const handleEditClick = (allergy) => {
        setFormData({
            name: allergy.name || "",
            img: allergy.img || "",
        });
        setCurrentAllergyId(allergy.id);
        setIsEditMode(true);
        setShowModal(true);
    };

    const handleCloseModal = () => {
        setShowModal(false);
        setIsEditMode(false);
        setFormData({
            name: "",
            img: "",
        });
        setCurrentAllergyId(null);
    };

    return (
        <>
            <div className="container">
                <div className="row mt-3 mb-3">
                    <h4 className="col-lg-8 col-md-8 col-sm-12">Alérgenos</h4>
                    <button className="col-lg-4 col-md-4 col-sm-12 btn btn-secondary float-right"
                        onClick={handleShowModal}>
                        Añadir alérgeno
                    </button>
                </div>
                <div className="row pl-o">
                    {store.allergies.map((item, index) => (
                        <div key={item.id} className="card col-lg-6 col-md-6 col-sm-12 p-1 mb-2">
                            <div className="card-header">
                                <h5>{item.name}</h5>
                            </div>
                            <div className="card-body row p-1 mb-2">
                                <div className="col-lg-4 col-md-3 col-sm-12 m-0">
                                    <img src={item.img} alt={item.name} />    
                                </div>
                                <div className="col-lg-8 col-md-9 col-sm-12">
                                    <div className="row">
                                        <h6 className="col-lg-8 col-md-8 col-sm-12">Ingredientes</h6>
                                        <span className="col-lg-4 col-md-4 col-sm-12 float-right">
                                            <i className={`fa-solid ${viewProducts[index] ? 'fa-minus' : 'fa-plus'}`}
                                                onClick={() => toggleExpand(index)}
                                                style={{ cursor: 'pointer' }}>
                                            </i>
                                        </span>
                                        {viewProducts[index] && (
                                            <ul className="list-group">
                                                {store.ingredients.filter(ingredient => item.id === ingredient.allergies_id).map((ingredient, key) => (
                                                    <li key={key} className="list-group-item pl-0 mb-4">{ingredient.name}</li>
                                                ))}
                                            </ul>
                                        )}
                                    </div>
                                    <button className="btn btn-outline-secondary btn-sm float-right"
                                        onClick={() => handleEditClick(item)}>Editar</button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
            {showModal && (
                <div className="modal fade show" style={{ display: "block" }}>
                    <div className="modal-dialog">
                        <div className="modal-content">
                            <div className="modal-header">
                                <h5 className="modal-title">
                                    {isEditMode ? "Editar alérgeno" : "Añadir alérgeno"}
                                </h5>
                                <button
                                    type="button"
                                    className="btn-close"
                                    onClick={handleCloseModal}
                                ></button>
                            </div>
                            <div className="modal-body">
                                <div className="mb-3">
                                    <label htmlFor="formName" className="form-label">Nombre</label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="formName"
                                        name="name"
                                        value={formData.name}
                                        onChange={handleChange}
                                        placeholder="Nombre del alérgeno"
                                    />
                                </div>
                                <div className="mb-3">
                                    <label htmlFor="formImage" className="form-label">Imagen</label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="formImage"
                                        name="img"
                                        value={formData.img}
                                        onChange={handleChange}
                                        placeholder="URL de la imagen"
                                    />
                                </div>
                            </div>
                            <div className="modal-footer">
                                <button
                                    type="button"
                                    className="btn btn-secondary"
                                    onClick={handleCloseModal}
                                >
                                    Cancelar
                                </button>
                                <button
                                    type="button"
                                    className="btn btn-primary"
                                    onClick={handleSubmit}
                                >
                                    Guardar
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            )}
        </>
    );
};