
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NumberOfEntitiesModule import NumberOfEntities







class NumberOfFiniteVolumeCells(NumberOfEntities):
    """
    Class representing the `NumberOfFiniteVolumeCells` entity, which inherits from:
    - NumberOfEntities

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_47608fd0_cc0d_457e_9141_051935029e3a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NumberOfFiniteVolumeCells'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NumberOfFiniteVolumeCells(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_47608fd0_cc0d_457e_9141_051935029e3a',
    
    class_name='NumberOfFiniteVolumeCells',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_47608fd0_cc0d_457e_9141_051935029e3a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NumberOfFiniteVolumeCells',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    