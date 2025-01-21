
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricSignalModule import ElectricSignal







class ElectricCurrentSignal(ElectricSignal):
    """
    Class representing the `ElectricCurrentSignal` entity, which inherits from:
    - ElectricSignal

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_904b12e0_4a10_47b0_b7db_592aba215cb6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricCurrentSignal'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricCurrentSignal(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_904b12e0_4a10_47b0_b7db_592aba215cb6',
    
    class_name='ElectricCurrentSignal',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_904b12e0_4a10_47b0_b7db_592aba215cb6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricCurrentSignal',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    