
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalSubstanceModule import ChemicalSubstance







class ChemicalCompound(ChemicalSubstance):
    """
    Class representing the `ChemicalCompound` entity, which inherits from:
    - ChemicalSubstance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e2b11f6a_4191_427e_9844_2e0ac88dfc8b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChemicalCompound'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChemicalCompound(
    
    class_iri='https://w3id.org/emmo#EMMO_e2b11f6a_4191_427e_9844_2e0ac88dfc8b',
    
    class_name='ChemicalCompound',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e2b11f6a_4191_427e_9844_2e0ac88dfc8b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChemicalCompound',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    