
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ConcentrationLimitModule import ConcentrationLimit







class MiniumumConcentration(ConcentrationLimit):
    """
    Class representing the `MiniumumConcentration` entity, which inherits from:
    - ConcentrationLimit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a9873707_8103_4bb4_9e51_83db1e89b1bd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MiniumumConcentration'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MiniumumConcentration(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a9873707_8103_4bb4_9e51_83db1e89b1bd',
    
    class_name='MiniumumConcentration',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a9873707_8103_4bb4_9e51_83db1e89b1bd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MiniumumConcentration',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    