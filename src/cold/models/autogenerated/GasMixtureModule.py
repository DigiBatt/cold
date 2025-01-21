
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GasModule import Gas



from .MixtureModule import Mixture







class GasMixture(Gas, Mixture):
    """
    Class representing the `GasMixture` entity, which inherits from:
    - Gas, Mixture

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_12a9a254_9791_4a00_b045_f397bc3ab2bc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GasMixture'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GasMixture(
    
    class_iri='https://w3id.org/emmo#EMMO_12a9a254_9791_4a00_b045_f397bc3ab2bc',
    
    class_name='GasMixture',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_12a9a254_9791_4a00_b045_f397bc3ab2bc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GasMixture',
        alias="class_name"
    )
    

    
    

    

    