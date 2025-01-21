
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricSignalModule import ElectricSignal







class ElectricPotentialSignal(ElectricSignal):
    """
    Class representing the `ElectricPotentialSignal` entity, which inherits from:
    - ElectricSignal

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0a03ce7e_d79f_412e_a103_b5d74de9f4d7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricPotentialSignal'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricPotentialSignal(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0a03ce7e_d79f_412e_a103_b5d74de9f4d7',
    
    class_name='ElectricPotentialSignal',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0a03ce7e_d79f_412e_a103_b5d74de9f4d7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricPotentialSignal',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    