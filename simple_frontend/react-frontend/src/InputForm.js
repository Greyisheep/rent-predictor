import React, { useState } from 'react';
import axios from 'axios';

function InputForm({ updateResult }) {
  const [inputs, setInputs] = useState({
    // Initialize the state with your input fields
    StrtName: '',
    Storeys: 0,
    Cheaperflrs: '',
    LgCond: 0,
    Age: 0,
    GenHouse: '',
    Parking: '',
    Distance: 0,
    Location: '',
    RdCond: 0,
    SecurityLvl: 0,
    RmSize: 0,
    RmCond: 0,
    Wdrobe: '',
    Finishing: '',
    Balcony: '',
    KitchenSize: 0,
    BathrmSize: 0,
    BalcnySize: 0,
    RefDisposal: null,
    LodgeGen: null,
    SecPost: null,
    Solar: null,
    RunWater: null,
    Cleaners: null,
    Electricity: null,
    ElecLodgeGen: null
    // Add other fields here
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8001/api/v1/predict', { inputs: [inputs] });
      if (response.status === 200) {
        updateResult(response.data);
      }
    } catch (error) {
      console.error(error);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setInputs({ ...inputs, [name]: value });
  };

  return (
    <div className="FormContainer"> {/* Add the FormContainer div */}
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="StrtName"
        value={inputs.StrtName}
        onChange={handleChange}
        placeholder="StrtName"
      />
      <input
        type="number"
        name="Storeys"
        value={inputs.Storeys}
        onChange={handleChange}
        placeholder="Storeys"
      />
      <input
        type="text"
        name="Cheaperflrs"
        value={inputs.Cheaperflrs}
        onChange={handleChange}
        placeholder="Cheaperflrs"
      />
      <input
        type="number"
        name="LgCond"
        value={inputs.LgCond}
        onChange={handleChange}
        placeholder="LgCond"
      />
      <input
        type="number"
        name="Age"
        value={inputs.Age}
        onChange={handleChange}
        placeholder="Age"
      />
      <input
        type="text"
        name="GenHouse"
        value={inputs.GenHouse}
        onChange={handleChange}
        placeholder="GenHouse"
      />
      <input
        type="text"
        name="Parking"
        value={inputs.Parking}
        onChange={handleChange}
        placeholder="Parking"
      />
      <input
        type="number"
        name="Distance"
        value={inputs.Distance}
        onChange={handleChange}
        placeholder="Distance"
      />
      <input
        type="text"
        name="Location"
        value={inputs.Location}
        onChange={handleChange}
        placeholder="Location"
      />
      <input
        type="number"
        name="RdCond"
        value={inputs.RdCond}
        onChange={handleChange}
        placeholder="RdCond"
      />
      <input
        type="number"
        name="SecurityLvl"
        value={inputs.SecurityLvl}
        onChange={handleChange}
        placeholder="SecurityLvl"
      />
      <input
        type="number"
        name="RmSize"
        value={inputs.RmSize}
        onChange={handleChange}
        placeholder="RmSize"
      />
      <input
        type="number"
        name="RmCond"
        value={inputs.RmCond}
        onChange={handleChange}
        placeholder="RmCond"
      />
      <input
        type="text"
        name="Wdrobe"
        value={inputs.Wdrobe}
        onChange={handleChange}
        placeholder="Wdrobe"
      />
      <input
        type="text"
        name="Finishing"
        value={inputs.Finishing}
        onChange={handleChange}
        placeholder="Finishing"
      />
      <input
        type="text"
        name="Balcony"
        value={inputs.Balcony}
        onChange={handleChange}
        placeholder="Balcony"
      />
      <input
        type="number"
        name="KitchenSize"
        value={inputs.KitchenSize}
        onChange={handleChange}
        placeholder="KitchenSize"
      />
      <input
        type="number"
        name="BathrmSize"
        value={inputs.BathrmSize}
        onChange={handleChange}
        placeholder="BathrmSize"
      />
      <input
        type="number"
        name="BalcnySize"
        value={inputs.BalcnySize}
        onChange={handleChange}
        placeholder="BalcnySize"
      />
      <input
        type="boolean"
        name="RefDisposal"
        value={inputs.RefDisposal}
        onChange={handleChange}
        placeholder="RefDisposal"
      />
      <input
        type="boolean"
        name="LodgeGen"
        value={inputs.LodgeGen}
        onChange={handleChange}
        placeholder="LodgeGen"
      />
      <input
        type="boolean"
        name="SecPost"
        value={inputs.SecPost}
        onChange={handleChange}
        placeholder="SecPost"
      />
      <input
        type="boolean"
        name="Solar"
        value={inputs.Solar}
        onChange={handleChange}
        placeholder="Solar"
      />
      <input
        type="boolean"
        name="RunWater"
        value={inputs.RunWater}
        onChange={handleChange}
        placeholder="RunWater"
      />
      <input
        type="boolean"
        name="Cleaners"
        value={inputs.Cleaners}
        onChange={handleChange}
        placeholder="Cleaners"
      />
        <input
          type="boolean"
          name="Electricity"
          value={inputs.Electricity}
          onChange={handleChange}
          placeholder="Electricity"
        />
      <input
        type="boolean"
        name="ElecLodgeGen"
        value={inputs.ElecLodgeGen}
        onChange={handleChange}
        placeholder="ElecLodgeGen"
      />
      {/* Add more input fields here */}
      <button type="submit">Submit</button>
    </form>
    </div>
  );
}

export default InputForm;
