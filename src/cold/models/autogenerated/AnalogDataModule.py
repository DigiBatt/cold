
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EncodedDataModule import EncodedData







class AnalogData(EncodedData):
    """
    Class representing the `AnalogData` entity, which inherits from:
    - EncodedData

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0d1c0018_42e2_4506_bc3d_f53c117c1ad3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AnalogData'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AnalogData(
    
    class_iri='https://w3id.org/emmo#EMMO_0d1c0018_42e2_4506_bc3d_f53c117c1ad3',
    
    class_name='AnalogData',
    
    elucidation="example_value",
    
    comment="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0d1c0018_42e2_4506_bc3d_f53c117c1ad3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AnalogData',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    