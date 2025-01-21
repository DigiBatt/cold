
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MatterModule import Matter







class OrdinaryMatter(Matter):
    """
    Class representing the `OrdinaryMatter` entity, which inherits from:
    - Matter

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6e9cb807_fc68_4bcf_b3ba_5fccc887c644'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'OrdinaryMatter'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = OrdinaryMatter(
    
    class_iri='https://w3id.org/emmo#EMMO_6e9cb807_fc68_4bcf_b3ba_5fccc887c644',
    
    class_name='OrdinaryMatter',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6e9cb807_fc68_4bcf_b3ba_5fccc887c644',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'OrdinaryMatter',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    