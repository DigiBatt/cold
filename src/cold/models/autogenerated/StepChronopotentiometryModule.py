
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChronopotentiometryModule import Chronopotentiometry







class StepChronopotentiometry(Chronopotentiometry):
    """
    Class representing the `StepChronopotentiometry` entity, which inherits from:
    - Chronopotentiometry

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#StepChronopotentiometry'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StepChronopotentiometry'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StepChronopotentiometry(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#StepChronopotentiometry',
    
    class_name='StepChronopotentiometry',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#StepChronopotentiometry',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StepChronopotentiometry',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    