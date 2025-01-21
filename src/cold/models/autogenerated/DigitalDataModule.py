
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DiscreteDataModule import DiscreteData







class DigitalData(DiscreteData):
    """
    Class representing the `DigitalData` entity, which inherits from:
    - DiscreteData

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4db96fb7_e9e0_466d_942b_f6f17bfdc145'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DigitalData'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DigitalData(
    
    class_iri='https://w3id.org/emmo#EMMO_4db96fb7_e9e0_466d_942b_f6f17bfdc145',
    
    class_name='DigitalData',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4db96fb7_e9e0_466d_942b_f6f17bfdc145',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DigitalData',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    