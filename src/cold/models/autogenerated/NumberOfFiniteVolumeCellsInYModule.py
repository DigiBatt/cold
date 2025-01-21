
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NumberOfFiniteVolumeCellsModule import NumberOfFiniteVolumeCells







class NumberOfFiniteVolumeCellsInY(NumberOfFiniteVolumeCells):
    """
    Class representing the `NumberOfFiniteVolumeCellsInY` entity, which inherits from:
    - NumberOfFiniteVolumeCells

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c2a85d02_c6b4_42df_b5ed_a9904ec34a5c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NumberOfFiniteVolumeCellsInY'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NumberOfFiniteVolumeCellsInY(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c2a85d02_c6b4_42df_b5ed_a9904ec34a5c',
    
    class_name='NumberOfFiniteVolumeCellsInY',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c2a85d02_c6b4_42df_b5ed_a9904ec34a5c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NumberOfFiniteVolumeCellsInY',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    