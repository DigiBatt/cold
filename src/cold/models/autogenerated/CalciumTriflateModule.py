
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CalciumSaltCompoundModule import CalciumSaltCompound







class CalciumTriflate(CalciumSaltCompound):
    """
    Class representing the `CalciumTriflate` entity, which inherits from:
    - CalciumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_0952b0ae_0067_4b42_812a_abb68c95a6f8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CalciumTriflate'`
        - **Alias**: `class_name`
    
    - `IUPACName` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IUPACName`
    
    - `pubChemReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `pubChemReference`
    
    - `standardInChI` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `standardInChI`
    
    - `molecularFormula` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `molecularFormula`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CalciumTriflate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_0952b0ae_0067_4b42_812a_abb68c95a6f8',
    
    class_name='CalciumTriflate',
    
    IUPACName="example_value",
    
    pubChemReference="example_value",
    
    standardInChI="example_value",
    
    molecularFormula="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_0952b0ae_0067_4b42_812a_abb68c95a6f8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CalciumTriflate',
        alias="class_name"
    )
    
    IUPACName: Optional[str] = Field(
        None,
        alias="IUPACName"
    )
    
    pubChemReference: Optional[str] = Field(
        None,
        alias="pubChemReference"
    )
    
    standardInChI: Optional[str] = Field(
        None,
        alias="standardInChI"
    )
    
    molecularFormula: Optional[str] = Field(
        None,
        alias="molecularFormula"
    )
    

    
    

    

    