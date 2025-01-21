
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ConstructionLanguageModule import ConstructionLanguage







class ConfigurationLanguage(ConstructionLanguage):
    """
    Class representing the `ConfigurationLanguage` entity, which inherits from:
    - ConstructionLanguage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3997e1f5_f478_4572_a030_4b8e7e5cc63a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ConfigurationLanguage'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ConfigurationLanguage(
    
    class_iri='https://w3id.org/emmo#EMMO_3997e1f5_f478_4572_a030_4b8e7e5cc63a',
    
    class_name='ConfigurationLanguage',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3997e1f5_f478_4572_a030_4b8e7e5cc63a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ConfigurationLanguage',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    