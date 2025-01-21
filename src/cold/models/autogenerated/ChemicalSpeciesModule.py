
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalModule import Chemical







class ChemicalSpecies(Chemical):
    """
    Class representing the `ChemicalSpecies` entity, which inherits from:
    - Chemical

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_cbcf8fe6_6da6_49e0_ab4d_00f737ea9689'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChemicalSpecies'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChemicalSpecies(
    
    class_iri='https://w3id.org/emmo#EMMO_cbcf8fe6_6da6_49e0_ab4d_00f737ea9689',
    
    class_name='ChemicalSpecies',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_cbcf8fe6_6da6_49e0_ab4d_00f737ea9689',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChemicalSpecies',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    