
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TemporallyFundamentalModule import TemporallyFundamental



from .PersistenceModule import Persistence







class Product(TemporallyFundamental, Persistence):
    """
    Class representing the `Product` entity, which inherits from:
    - TemporallyFundamental, Persistence

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_82fc8506_1f84_4add_9683_abea077bd1e3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Product'`
        - **Alias**: `class_name`
    
    - `ISO9000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO9000Reference`
    
    - `ISO14040Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO14040Reference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Product(
    
    class_iri='https://w3id.org/emmo#EMMO_82fc8506_1f84_4add_9683_abea077bd1e3',
    
    class_name='Product',
    
    ISO9000Reference="example_value",
    
    ISO14040Reference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_82fc8506_1f84_4add_9683_abea077bd1e3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Product',
        alias="class_name"
    )
    
    ISO9000Reference: Optional[str] = Field(
        None,
        alias="ISO9000Reference"
    )
    
    ISO14040Reference: Optional[str] = Field(
        None,
        alias="ISO14040Reference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    