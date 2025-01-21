
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StrontiumSaltCompoundModule import StrontiumSaltCompound







class StrontiumTetrafluoroborate(StrontiumSaltCompound):
    """
    Class representing the `StrontiumTetrafluoroborate` entity, which inherits from:
    - StrontiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_a67cda39_f3ac_4983_a93d_07a2067b5901'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StrontiumTetrafluoroborate'`
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
    obj = StrontiumTetrafluoroborate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_a67cda39_f3ac_4983_a93d_07a2067b5901',
    
    class_name='StrontiumTetrafluoroborate',
    
    IUPACName="example_value",
    
    pubChemReference="example_value",
    
    standardInChI="example_value",
    
    molecularFormula="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_a67cda39_f3ac_4983_a93d_07a2067b5901',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StrontiumTetrafluoroborate',
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
    

    
    

    

    