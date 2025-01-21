
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DataFilteringModule import DataFiltering







class OutlierRemoval(DataFiltering):
    """
    Class representing the `OutlierRemoval` entity, which inherits from:
    - DataFiltering

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#OutlierRemoval'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'OutlierRemoval'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = OutlierRemoval(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#OutlierRemoval',
    
    class_name='OutlierRemoval',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#OutlierRemoval',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'OutlierRemoval',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    