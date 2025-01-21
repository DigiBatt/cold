
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ReductionisticModule import Reductionistic







class Tile(Reductionistic):
    """
    Class representing the `Tile` entity, which inherits from:
    - Reductionistic

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9953c19f_ee33_4af8_be5e_dbf6d1e33581'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Tile'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Tile(
    
    class_iri='https://w3id.org/emmo#EMMO_9953c19f_ee33_4af8_be5e_dbf6d1e33581',
    
    class_name='Tile',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9953c19f_ee33_4af8_be5e_dbf6d1e33581',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Tile',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    