
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EncodedDataModule import EncodedData







class ClassicalData(EncodedData):
    """
    Class representing the `ClassicalData` entity, which inherits from:
    - EncodedData

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ed257e78_8b59_44c3_9d61_06c261184f55'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ClassicalData'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ClassicalData(
    
    class_iri='https://w3id.org/emmo#EMMO_ed257e78_8b59_44c3_9d61_06c261184f55',
    
    class_name='ClassicalData',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ed257e78_8b59_44c3_9d61_06c261184f55',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ClassicalData',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    