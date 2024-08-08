import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/lists.css";

export const IngredientsList = () => {

const {store, actions} = useContext(Context)


    return (
        <ul className="list-group overflow-auto">
            {store.ingredients.map((item, index) => (
                <li key={index} className="list-group-item mb-4 card">
                        <div className="col-lg-8 col-md-9 col-sm-12">
                            <h6>{item.name}</h6>  
                            <p>{item.price}€</p>
                            {store.allergies.filter(allergy => item.allergies_id === allergy.id).map((allergy, key) => (
                                    <p key={key}>{allergy.name}</p>
                            ))}
                        </div>
                </li>
            )
            )}
        </ul>
    )
}

