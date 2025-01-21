
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CurrentControlledProcessModule import CurrentControlledProcess







class StrippingChronopotentiometry(CurrentControlledProcess):
    """
    Class representing the `StrippingChronopotentiometry` entity, which inherits from:
    - CurrentControlledProcess

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bfbefff0_4df5_47c2_9943_5f42cf268e9e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StrippingChronopotentiometry'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StrippingChronopotentiometry(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bfbefff0_4df5_47c2_9943_5f42cf268e9e',
    
    class_name='StrippingChronopotentiometry',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bfbefff0_4df5_47c2_9943_5f42cf268e9e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StrippingChronopotentiometry',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    