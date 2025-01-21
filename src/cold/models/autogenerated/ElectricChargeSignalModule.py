
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricSignalModule import ElectricSignal







class ElectricChargeSignal(ElectricSignal):
    """
    Class representing the `ElectricChargeSignal` entity, which inherits from:
    - ElectricSignal

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_276cfa84_3cc0_40c0_9f6a_57a3b776f47c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricChargeSignal'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricChargeSignal(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_276cfa84_3cc0_40c0_9f6a_57a3b776f47c',
    
    class_name='ElectricChargeSignal',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_276cfa84_3cc0_40c0_9f6a_57a3b776f47c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricChargeSignal',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    