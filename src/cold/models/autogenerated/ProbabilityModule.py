
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RatioQuantityModule import RatioQuantity







class Probability(RatioQuantity):
    """
    Class representing the `Probability` entity, which inherits from:
    - RatioQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0a88be81_343d_4388_92c1_09228ff95ada'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Probability'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Probability(
    
    class_iri='https://w3id.org/emmo#EMMO_0a88be81_343d_4388_92c1_09228ff95ada',
    
    class_name='Probability',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0a88be81_343d_4388_92c1_09228ff95ada',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Probability',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    