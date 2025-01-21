
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NumberOfFiniteVolumeCellsModule import NumberOfFiniteVolumeCells







class NumberOfFiniteVolumeCellsInZ(NumberOfFiniteVolumeCells):
    """
    Class representing the `NumberOfFiniteVolumeCellsInZ` entity, which inherits from:
    - NumberOfFiniteVolumeCells

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a5e00e3a_736c_4200_8d04_ed222fe07037'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NumberOfFiniteVolumeCellsInZ'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NumberOfFiniteVolumeCellsInZ(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a5e00e3a_736c_4200_8d04_ed222fe07037',
    
    class_name='NumberOfFiniteVolumeCellsInZ',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a5e00e3a_736c_4200_8d04_ed222fe07037',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NumberOfFiniteVolumeCellsInZ',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    