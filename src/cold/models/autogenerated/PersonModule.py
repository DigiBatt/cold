
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from ..custom.LinkedDataModelModule import LinkedDataModel







class Person(LinkedDataModel):
    """
    Class representing the `Person` entity, which inherits from:
    - LinkedDataModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://schema.org/Person'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Person'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Person(
    
    class_iri='https://schema.org/Person',
    
    class_name='Person',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://schema.org/Person',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Person',
        alias="class_name"
    )
    

    
    

    

    