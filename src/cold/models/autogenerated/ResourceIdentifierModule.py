
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from ..custom.LinkedDataModelModule import LinkedDataModel







class ResourceIdentifier(LinkedDataModel):
    """
    Class representing the `ResourceIdentifier` entity, which inherits from:
    - LinkedDataModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'http://purl.org/spar/datacite/ResourceIdentifier'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ResourceIdentifier'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ResourceIdentifier(
    
    class_iri='http://purl.org/spar/datacite/ResourceIdentifier',
    
    class_name='ResourceIdentifier',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'http://purl.org/spar/datacite/ResourceIdentifier',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ResourceIdentifier',
        alias="class_name"
    )
    

    
    

    

    