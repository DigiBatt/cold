
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalRepresentationModule import ChemicalRepresentation







class StructuralFormula(ChemicalRepresentation):
    """
    Class representing the `StructuralFormula` entity, which inherits from:
    - ChemicalRepresentation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a466b60b_d973_4b8f_897f_d0b837a59df3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StructuralFormula'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StructuralFormula(
    
    class_iri='https://w3id.org/emmo#EMMO_a466b60b_d973_4b8f_897f_d0b837a59df3',
    
    class_name='StructuralFormula',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a466b60b_d973_4b8f_897f_d0b837a59df3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StructuralFormula',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    